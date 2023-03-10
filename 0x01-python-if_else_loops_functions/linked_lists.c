#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new 
 * @head: pointer to head node
 * @n: interger data to be added to node
 * Return: address of new node or NULL if fails
 *
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;
	
	current = *head;
	
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	
	new->n = n;
	new->next = NULL;
	
	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		while(current->next != NULL)
			current = current->next;
		current->next = new;
	}
	
	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while(head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
