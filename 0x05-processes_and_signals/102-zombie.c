#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - entry poin
 *
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t pd;

	for (i = 0; i < 5; i++)
	{
		pd = fork();

		if (pd == 0)
			exit(0);
		else
			printf("Zombie process created, PID: ZOMBIE_PID: %d\n", pd);
	}
	infinite_while();
	return (0);
}
