#include "lists.h"


/**
 * insert_node - insert a node in a linked list (sorted)
 * @head: pointer to a list
 * @number: the value of the node
 *
 * Return: pointer to a new node or 0
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *current;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	current = *head;
	new->n = number;
	new->next = NULL;
	temp = NULL;
	while (current && current->n < number)
	{
		temp = current;
		current = current->next;
	}
	new->next = current;
	if (temp)
		temp->next = new;
	else
		*head = new;
	return (new);
}
