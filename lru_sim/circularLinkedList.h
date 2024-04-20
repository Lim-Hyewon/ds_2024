typedef struct ListNode {
    char* item;
    struct ListNode* next;
} ListNode;

typedef struct CircularLinkedList {
    ListNode* tail;
    int numItems;
} CircularLinkedList;

void initCircularLinkedList(CircularLinkedList* list);

void append(CircularLinkedList* list, char* newItem);

char* pop(CircularLinkedList* list);

char* removeItem(CircularLinkedList* list, char* x); 

int index(CircularLinkedList* list, char* x);

int size(CircularLinkedList* list);

typedef struct CircularLinkedListIterator {
    ListNode* head;
    ListNode* iterPosition;
} CircularLinkedListIterator;

void initCircularLinkedListIterator(CircularLinkedListIterator* iterator, CircularLinkedList* list);

char* next(CircularLinkedListIterator* iterator);