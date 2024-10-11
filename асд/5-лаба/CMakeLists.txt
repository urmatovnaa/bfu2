cmake_minimum_required(VERSION 3.15) 	# Проверка версии CMake.
					# Если версия установленой программы
					# старее указаной, произайдёт аварийный выход.

set(PROJECT_NAME rebb)		# имя проекта		 
project("${PROJECT_NAME}")


set(CMAKE_CXX_STANDARD 17)		# устанавливаем 17 стандарт языка
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)


set(SRC_LIST 5-laba.cpp)

add_executable(${PROJECT_NAME} ${SRC_LIST})