#include "lists.h"

/**
 * check_cycle - hecks if a singly linked list has a cycle in it
 * @list: pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	size_t arr_size = 100;
	int idx = 1, i;
	listint_t **arr, **arr_cpy;

	arr = (listint_t **) malloc(arr_size * sizeof(listint_t *));
	arr[0] = list;
	while (list->next != NULL)
	{
		if (idx == arr_size)
		{
			arr_size += 100;
			arr_cpy = (listint_t **) malloc(arr_size * sizeof(lisint_t *));
			for (i = 0; i < idx; i++)
			{
				arr_cpy[idx] = arr[idx];
			}
			free(arr);
			arr = arr_cpy;
			arr_cpy = NULL;
		}
		for (i = 0; i < idx; i++)
		{
			if (arr[i] == list->next)
			{
				free(arr);
				return (1);
			}
		}
		arr[idx++] = list->next;
		list = list->next;
	}
	free(arr);
	return (0);
}
