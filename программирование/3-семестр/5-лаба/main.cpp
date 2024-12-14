#include <SFML/Graphics.hpp>
#include <cmath>

#include "graph.cpp"

using namespace std;


void adjacency_matrix(vector<pair<int, int>> m_edges, int n){
    int max_v = n;

    vector<vector<int>> matrix(max_v, vector<int>(max_v, 0));

    for (const auto& edge : m_edges) {
        int from = edge.first - 1;
        int to = edge.second - 1;
        matrix[from][to] = 1;     
    }

    int i = 1;
    std::cout << "Матрица смежности:\n";
    for (int j = 0; j <= max_v; j++){
        if (j){cout << j << " ";}
        else {cout << "  ";}
    }
    cout << "\n";
    for (const auto& row : matrix) {
        cout << i << " ";
        for (int value : row) {
            std::cout << value << " ";
        }
        std::cout << "\n";
        i++;
    }
}

void adjacency_list(vector<pair<int, int>> m_edges, int n){
    int max_v = n;
    vector<vector<int>> adj_list(max_v);

    for (auto edge : m_edges) {
        int from = edge.first - 1;
        int to = edge.second;
        adj_list[from].push_back(to);
    }
    std::cout << "Список смежности:\n";
    for (int i = 0; i < max_v; i++) {
        cout << i + 1 << ": ";
        for (int neighbor : adj_list[i]) {
            cout << neighbor << " ";
        }
        cout << endl;
    }
}

void edge_list(vector<pair<int, int>> m_edges){
    std::cout << "Список ребер:\n";
    for (auto edge : m_edges) {
        cout << "{" << edge.first << "," << edge.second << "}" << " ";
    }
    cout << endl;
}

int main()
{   srand(time(0));
	sf::RenderWindow m_window;
	int width = 800;
	int height = 800;
	m_window.create(sf::VideoMode(width, height), "Graph!!!!");
	sf::WindowHandle handle = m_window.getSystemHandle();

    std::vector<std::pair<int, int>> edges = {
        {1, 2}, {1, 3},
        {2, 5},
        {3, 4}, {3, 5},
        {5, 6},
        {6, 1}, {6, 5}
    };

    int triangles_count = edges.size();

    int Number_Vertices = 7;
    int radius = 25;
    std::vector<sf::Color> triangleColors = generateUniqueColors(triangles_count);

    mt::Circle circles[Number_Vertices];
    mt::Circle circle(0, 0, 0, 0);

    for (short i = 1; i <= Number_Vertices; i++){
        float angle = 2 * M_PI * i / Number_Vertices;
        float x = 400 + 200 * cos(angle);
        float y = 400 + 200 * sin(angle);
        circle.Setup(x, y, radius, i);
        circles[i - 1] = circle;
    }

    TriangleShape triangles[triangles_count]; 
    int triangleCount = 0; 

    for (int i = 0; i < triangles_count; i++) {
        int u = edges[i].first - 1;
        int v = edges[i].second - 1;
        triangles[triangleCount] = createTriangle(circles[u], circles[v], triangleColors[i]);
        triangleCount++;
    }

	while (m_window.isOpen())
	{
		sf::Event event;
		while (m_window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				m_window.close();
		}
        m_window.clear(sf::Color::White);
        for (int i = 0; i < triangleCount; i++) {
            m_window.draw(triangles[i].shape);
        }
        for (int i = 0; i < Number_Vertices; i++) {
            circles[i].draw(m_window);
        }
		m_window.display();
	};
    
    
    // Список ребер
    edge_list(edges);
    // Матрица смежности
    adjacency_matrix(edges, Number_Vertices);

    // Список смежности
    adjacency_list(edges, Number_Vertices);

	return 0;
}