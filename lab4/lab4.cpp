#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

struct list {
	int field; // поле данних
	struct list *next; // вказівник на наступний елемент
	struct list *prev; // вказівник на попередній елемент
};

struct list * init(int a) { // а- значення першого вузла
	struct list *lst;
	// виділення памяті під корінь списку
	lst = (struct list*)malloc(sizeof(struct list));
	lst->field = a;
	lst->next = NULL; // вказівник на наступний вузол
	lst->prev = NULL; // вказівник на попередній вузол
	return(lst);
}

struct list * addelem(list *lst, int number) {
	struct list *temp, *p;
	temp = (struct list*)malloc(sizeof(list));
	p = lst->next; // зббереження наступного елемента
	lst->next = temp; // попередній вузол вказує на створений
	temp->field = number; // збереження поля даних доданого вузла
	temp->next = p; // створений вузол вказує на наступний вузол
	temp->prev = lst; // створений вузол вказує на поередній вузол
	if (p != NULL)
		p->prev = temp;
	return(temp);
}

struct list * deletelem(list *lst) {
	struct list *prev, *next;
	prev = lst->prev; // вузол перед lst
	next = lst->next; // вузол після lst
	if (prev != NULL)
		prev->next = lst->next; // переставляєм вказівник
	if (next != NULL)
		next->prev = lst->prev;
	free(lst); // звільняємо пам'ять виділеного вузла
	return(prev);
}

void listprint(list *lst) {
	struct list *p;
	p = lst;
	do {
		printf("%d ", p->field); // вивід значення вузла р
		p = p->next; // перехід до наступного вузла
	} while (p != NULL);
}

int main() {
	list *head, *cur;
	int num;
	head = init(3);
	cur = head;
    cur = addelem(cur, 8);
    cur = addelem(cur, 1);
	cur = addelem(cur, 100);
    cur = addelem(cur, 4);
	cur = addelem(cur, 10);
	// for (int i = 0; i < 5; i++) {
	// 	// printf("a = ");
	// 	// scanf("%d", &num);
	// 	cur = addelem(cur, i);
	// }
    listprint(head);
	// // Удаляем третий элемент списка
	// cur = head->next->next;
	// deletelem(cur);
	// listprint(head);
	// getchar();
	return 0;
}