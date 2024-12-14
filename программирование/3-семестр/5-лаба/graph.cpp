#pragma once
#include <SFML/Graphics.hpp>
#include <iostream>
#include <typeinfo>
#include <cmath>

using namespace std;
using namespace sf;

namespace mt
{
	class Circle
	{  
		sf::CircleShape m_shape;
        sf::Text text;
        sf::Font font;

	public:
		Circle() = default;

		Circle(float x, float y, float r, short number)
		{
			Setup(x, y, r, number);
		}

		void Setup(float x, float y, float r, short number)
		{
			m_shape.setOrigin(r, r);
			m_shape.setRadius(r);
			m_shape.setPosition(x, y);
            m_shape.setFillColor(sf::Color::Blue);
            if (!font.loadFromFile("font1.ttf")) {
                std::cerr << "Не удалось загрузить шрифт" << std::endl;
            }
            // Инициализация текста
            text.setFont(font);
            text.setString(std::to_string(number)); // Число внутри круга
            text.setCharacterSize(40);
            text.setFillColor(sf::Color::White);
            
            // Центрируем текст внутри круга
            sf::FloatRect textBounds = text.getLocalBounds();
            text.setOrigin(textBounds.left + textBounds.width / 2, textBounds.top + textBounds.height / 2);
            text.setPosition(x, y);
        }

		void draw(sf::RenderWindow& window) const {
            window.draw(m_shape);  // Рисуем круг
            window.draw(text);    // Рисуем текст
        }
        sf::CircleShape get_circle(){
            return m_shape;
        }
	};

}

struct TriangleShape {
    VertexArray shape;
    Color m_color;

    TriangleShape(Vector2f point1, Vector2f point2, Vector2f point3, Color color) {
        m_color = color;
        shape.setPrimitiveType(Triangles);
        shape.append(Vertex(point1, color));
        shape.append(Vertex(point2, color));
        shape.append(Vertex(point3, color));
    }
    
    TriangleShape() {
        shape.setPrimitiveType(Triangles);
    }
    Color get_color(){return m_color;}
};

Color randomColor() {
    return Color(rand() % 256, rand() % 256, rand() % 256);
}


TriangleShape createTriangle(mt::Circle& circle1, mt::Circle& circle2, Color color) {
    Vector2f center1 = circle1.get_circle().getPosition();
    Vector2f center2 = circle2.get_circle().getPosition();

    float radius1 = circle1.get_circle().getRadius();
    float radius2 = circle2.get_circle().getRadius();

    Vector2f direction = center2 - center1;
    float angle = atan2(direction.y, direction.x);

    Vector2f point1(center1.x + radius1 * cos(angle - M_PI / 2), center1.y + radius1 * sin(angle - M_PI / 2));
    Vector2f point2(center1.x + radius1 * cos(angle + M_PI / 2), center1.y + radius1 * sin(angle + M_PI / 2));
    Vector2f point3(center2.x - radius2 * cos(angle), center2.y - radius2 * sin(angle));

    return TriangleShape(point1, point2, point3, color);
}

std::vector<sf::Color> generateUniqueColors(int count) {
    std::vector<sf::Color> uniqueColors;

    while (uniqueColors.size() < count) {
        sf::Color newColor = randomColor();
        bool exists = false;

        // Проверяем, есть ли цвет в массиве
        for (const auto& color : uniqueColors) {
            if (color == newColor) {
                exists = true;
                break;
            }
        }

        // Если цвета нет, добавляем
        if (!exists) {
            uniqueColors.push_back(newColor);
        }
    }

    return uniqueColors;
}