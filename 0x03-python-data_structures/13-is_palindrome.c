#include "lists.h"
#include <stdio.h>

int length_of_list(listint_t **head);
listint_t *get_node_at_index(listint_t **head, int index);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of linked list
 *
 * Return: 1 if list is a palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	listint_t *comp = NULL;
	int i = 0;
	int len;

	if (!head)
		return (1);

	if (*head == NULL)
		return (1);

	len = length_of_list(head);
	printf("len: %d\n", len);
	current = *head;

	for (i = 0; i <= (len - 1) / 2; i++)
	{
		comp = get_node_at_index(head, (len - i - 1));

		if (comp->n != current->n)
			return (0);

		current = current->next;
	}

	return (1);
}

/**
 * get_node_at_index - returns pointer to node at a specific index
 * @head: pointer to pointer to head of linked list
 * @index: index of node to return
 *
 * Return: pointer to node at specified index
 */
listint_t *get_node_at_index(listint_t **head, int index)
{
	listint_t *current;
	int i = 0;

	current = *head;

	while (current->next && i != index)
	{
		current = current->next;
		i++;
	}

	return (current);
}

/**
 * length_of_list - gets length of linked list
 * @head: pointer to pointer to head of linked list
 *
 * Return: length of linked list
 */
int length_of_list(listint_t **head)
{
	listint_t *current;
	int i = 0;

	current = *head;

	while (current)
	{
		current = current->next;
		i++;
	}

	return (i);
}
