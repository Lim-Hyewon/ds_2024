// Define ListNode structure
typedef struct ListNode {
    char* item;
    struct ListNode* next;
} ListNode;

// Define CircularLinkedList structure
typedef struct CircularLinkedList {
    ListNode* tail;
    int numItems;
} CircularLinkedList;

// Initialize CircularLinkedList
void initCircularLinkedList(CircularLinkedList* list);

// Append a new item to the CircularLinkedList
void append(CircularLinkedList* list, char* newItem);

// Remove the last item from the CircularLinkedList
char* pop(CircularLinkedList* list);

// Remove a specific item from the CircularLinkedList
char* removeItem(CircularLinkedList* list, char* x); 

// Get the index of a specific item in the CircularLinkedList
int index(CircularLinkedList* list, char* x);

// Get the size of the CircularLinkedList
int size(CircularLinkedList* list);

// Define CircularLinkedListIterator structure
typedef struct CircularLinkedListIterator {
    ListNode* head;
    ListNode* iterPosition;
} CircularLinkedListIterator;

// Initialize CircularLinkedListIterator
void initCircularLinkedListIterator(CircularLinkedListIterator* iterator, CircularLinkedList* list);

// Get the next item in the CircularLinkedListIterator
char* next(CircularLinkedListIterator* iterator);