#include <iostream>

using namespace std;

int possible_moves[9];
int mat[6][6];

void initialize_matrix()
{
	for (int i = 0; i < 6; ++i)
	{
		for (int j = 0; j < 6; ++j)
		{
			mat[i][j] = 0;
		}
	}

	for (int i = 0; i < 6; ++i)
	{
		mat[0][i] = 5;
		mat[i][0] = 5;
		mat[5][i] = 5;
		mat[i][5] = 5;
	}

	for (int i = 1; i <= 4; ++i)
	{
		mat[1][i] = 1;
	}

	for (int i = 1; i <= 4; ++i)
	{
		mat[4][i] = 2;
	}
}

void show_board()
{
	for (int i = 0; i < 6; ++i)
	{
		for (int j = 0; j < 6; ++j)
		{
			if (mat[i][j] == 1)
			{
				cout << " x ";
			}

			if (mat[i][j] == 2)
			{
				cout << " o ";
			}

			if (mat[i][j] == 0)
			{
				cout << "   ";
			}

			if (mat[i][j] == 5)
			{
				cout << " . ";
			}
		}
		cout << endl;
	}
}

int is_valid_move(int ln1, int col1, int ln2, int col2)
{
	if ((abs(ln1 - ln2) == 1 && abs(col1 - col2) == 1 && mat[ln2][col2] == 0) ||
		(abs(ln1 - ln2) == 1 && abs(col1 - col2) == 0 && mat[ln2][col2] == 0) ||
		(abs(ln1 - ln2) == 0 && abs(col1 - col2) == 1 && mat[ln2][col2] == 0))
	{
		return 1;
	}
	return 0;
}

void make_manual_move(int ln1, int col1, int ln2, int col2, int turn)
{
	if (is_valid_move(ln1, col1, ln2, col2) == 1)
	{
		mat[ln2][col2] = turn;
		mat[ln1][ln2] = 0;
	}
}

int is_final_state()
{
	for (int i = 1; i <= 4; ++i)
	{
		if (mat[1][i] == 2)
		{
			cout << "o won!" << endl;
			return 1;
		}
	}

	for (int i = 1; i <= 4; ++i)
	{
		if (mat[4][i] == 1)
		{
			cout << "x won!" << endl;
			return 1;
		}
	}

	return 0;
}

void make_move(int ln, int col, int random_move, int turn)
{
	mat[ln][col] = 0;

	if (random_move == 0)
	{
		mat[ln - 1][col - 1] = turn;
	}
	if (random_move == 1)
	{
		mat[ln - 1][col] = turn;
	}
	if (random_move == 2)
	{
		mat[ln - 1][col + 1] = turn;
	}
	if (random_move == 3)
	{
		mat[ln][col + 1] = turn;
	}
	if (random_move == 4)
	{
		mat[ln + 1][col + 1] = turn;
	}
	if (random_move == 5)
	{
		mat[ln + 1][col] = turn;
	}
	if (random_move == 6)
	{
		mat[ln + 1][col - 1] = turn;
	}
	if (random_move == 6)
	{
		mat[ln][col - 1] = turn;
	}
}

//possible_moves[0] is top left
//possible_moves[1] is top 
//possible_moves[2] is top right
//possible_moves[3] is right
//possible_moves[4] is bottom right 
//possible_moves[5] is bottom
//possible_moves[6] is bottom left 
//possible_moves[7] is left

int make_random_move(int ln, int col, int turn)
{
	if (mat[ln - 1][col - 1] == 0)
	{
		possible_moves[0] = 1;
	}
	if (mat[ln - 1][col] == 0)
	{
		possible_moves[1] = 1;
	}
	if (mat[ln - 1][col + 1] == 0)
	{
		possible_moves[2] = 1;
	}
	if (mat[ln][col + 1] == 0)
	{
		possible_moves[3] = 1;
	}
	if (mat[ln + 1][col + 1] == 0)
	{
		possible_moves[4] = 1;
	}
	if (mat[ln + 1][col] == 0)
	{
		possible_moves[5] = 1;
	}
	if (mat[ln + 1][col - 1] == 0)
	{
		possible_moves[6] = 1;
	}
	if (mat[ln][col - 1] == 0)
	{
		possible_moves[7] = 1;
	}

	int is_ok = 0;
	int random_move;

	while (!is_ok)
	{
		random_move = rand() % 7;
		if (possible_moves[random_move] == 1)
		{
			is_ok = 1;
			cout << "The move is possible." << endl;
			make_move(ln, col, random_move, turn);
			return 1;
		}
		
	}

	for (int i = 0; i < 8; ++i)
	{
		possible_moves[i] = 0;
	}

	return 0;
}

int main()
{
	initialize_matrix();	
	show_board();

	cout << endl;

	make_manual_move(1, 1, 2, 1, 1);
	show_board();

	cout << endl;

	make_random_move(4, 1, 2);
	show_board();

	system("pause");
	return 0;
}