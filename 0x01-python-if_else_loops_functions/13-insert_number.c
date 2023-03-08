#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts node a position in a sorted listint
 * @head: pointer to first node of list
 * @number: int to add to list
 * Return: Address of new node;
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	current = *head;
	if (current == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		if (current->n > number)
		{
			new->next = current;
			*head = new;
		}
		else
		{
			while (current->next != NULL)
			{
				if (current->next->n > number)
				{
					new->next = current->next;
					current->next = new;
					return (new);
				}
				current = current->next;
			}
			current->next = new;
			new->next = NULL;
		}
	}
	return (new);
}
