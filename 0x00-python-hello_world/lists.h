#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 0 if it doesn't, 1 if the list has a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

if (!list)
return (0);

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}

return (0);
}
root@e024474929d2:~/alx-higher_level_programming/0x00-python-hello_world# cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Singly linked list
 * @n: integer
 * @next: Points to the next node
 *
 * Description: Singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
