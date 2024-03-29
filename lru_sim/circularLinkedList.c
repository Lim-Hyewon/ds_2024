#include <stdlib.h>
#include <string.h>
#include "circularLinkedList.h"


void initCircularLinkedList(CircularLinkedList* list) {
    list->tail = NULL;
    list->numItems = 0;
}

void append(CircularLinkedList* list, char* newItem) {
    ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->item = newItem;
    if (list->tail == NULL) {
        newNode->next = newNode;
        list->tail = newNode;
    } else {
        newNode->next = list->tail->next;
        list->tail->next = newNode;
        list->tail = newNode;
    }
    list->numItems++;
}

char* pop(CircularLinkedList* list) {
    if (list->numItems == 0) {
        return NULL;
    }
    ListNode* prev = list->tail->next;
    char* retItem = prev->item;
    prev->next = prev->next->next;
    if (list->numItems == 1) {
        list->tail = NULL;
    } else if (list->numItems == 2) {
        list->tail = prev;
    }
    list->numItems--;
    return retItem;
}

char* removeItem(CircularLinkedList* list, char* x) {
    if (list->numItems == 0) {
        return NULL;
    }
    ListNode* prev = list->tail;
    ListNode* curr = prev->next;
    do {
        if (strcmp(curr->item, x) == 0) {
            prev->next = curr->next;
            if (curr == list->tail) {
                list->tail = prev;
            }
            list->numItems--;
            return x;
        }
        prev = curr;
        curr = curr->next;
    } while (curr != list->tail->next);
    return NULL;
}

int index(CircularLinkedList* list, char* x) {
    int cnt = 0;
    ListNode* curr = list->tail;
    if (curr == NULL)
        return -2;
    do {
        if (strcmp(curr->item, x) == 0)
            return cnt;
        curr = curr->next;
        cnt++;
    } while (curr != list->tail);
    return -2;
}

int size(CircularLinkedList* list) {
    return list->numItems;
}

void initCircularLinkedListIterator(CircularLinkedListIterator* iterator, CircularLinkedList* list) {
    iterator->head = list->tail->next;
    iterator->iterPosition = iterator->head;
}

char* next(CircularLinkedListIterator* iterator) {
    if (iterator->iterPosition == iterator->head) {
        return NULL;
    } else {
        char* item = iterator->iterPosition->item;
        iterator->iterPosition = iterator->iterPosition->next;
        return item;
    }
}