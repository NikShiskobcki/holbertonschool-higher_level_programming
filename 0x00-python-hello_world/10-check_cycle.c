#include "lists.h"
/**
 * check_cycle - checks for loop
 * @list: input list
 * Return: 1 if loop, 0 if no loop
 */
int check_cycle(listint_t *list)
{
listint_t *ptr1 = list; /*fast pointer*/
listint_t *ptr2 = list; /*slow pointer*/

	while (ptr1 && ptr2 && ptr1->next)
	{
		ptr1 = ptr1->next->next;
		ptr2 = ptr2->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
