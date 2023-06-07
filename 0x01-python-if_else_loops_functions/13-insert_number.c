#include "lists.h"

/**
 * 
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, prev;

	node = (listint_t *) malloc(sizeof(listint_t *));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	prev = *head;
	while (prev->next != NULL && prev->next->n < number)
		prev = prev->next;
	node->next = prev->next;
	prev->next = node;
	return (node);
}
