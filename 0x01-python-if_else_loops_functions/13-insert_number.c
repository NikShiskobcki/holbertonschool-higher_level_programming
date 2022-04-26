#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node
 * @head: input
 * @number: input
 * Return: adress of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *aux;
	aux = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (!aux || aux->n >=number)
	{
		new_node->next = aux;
		*head = new_node;
		return (new_node);
	}
	while (aux && aux->next && aux->next->n < number)
		aux = aux->next;
	new_node->next = aux->next;
	aux->next = new_node;

	return(new_node);

}
