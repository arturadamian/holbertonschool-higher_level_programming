#include "lists.h"


/**
 * check_cycle - checks the linked list if it is a cycle
 * @list: pointer to a list
 *
 * Return: 1 if cucle or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *step;
	listint_t *step2;

	if (list == NULL)
		return (0);
	step = list;
	step2 = list;
	while (step2 != NULL)
	{
		step = step->next;
		step2 = step2->next->next;
		if (step == step2)
			return (1);
	}
	return (0);
}
