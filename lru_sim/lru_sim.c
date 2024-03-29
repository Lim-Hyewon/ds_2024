#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "circularLinkedList.h"

#define INITIAL_CAPACITY 10000
#define INCREMENT_SIZE 10000

typedef struct CacheSimulator {
    int cache_slots;
    int cache_hit;
    int tot_cnt;
    CircularLinkedList container;
} CacheSimulator;

void do_sim(CacheSimulator* sim, char* page) {
    sim->tot_cnt++;
    if (index(&(sim->container), page) != -2) {
        sim->cache_hit++;
        // printf("%s\n", page);
        removeItem(&(sim->container), page);
        append(&(sim->container), page);
        return;
    }
    append(&(sim->container), page);
    if (size(&(sim->container)) >= sim->cache_slots)
        pop(&(sim->container));
}

void print_stats(CacheSimulator* sim) {
    printf("cache slots = %d ", sim->cache_slots);
    printf("cache hits = %d ", sim->cache_hit);
    printf("hit ratio = %.5f\n", (float)sim->cache_hit / sim->tot_cnt);
}

int main() {
    FILE* data_file = fopen("./linkbench.trc", "r");
    if (data_file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[256];
    int capacity = INITIAL_CAPACITY;
    char** lines = (char**)malloc(capacity * sizeof(char*));
    int lines_count = 0;

    while (fgets(line, sizeof(line), data_file) != NULL) {
        line[strcspn(line, "\n")] = 0;
        if (lines_count >= capacity) {
            capacity += INCREMENT_SIZE;
            lines = (char**)realloc(lines, capacity * sizeof(char*));
            if (lines == NULL) {
                perror("Error reallocating memory");
                return 1;
            }
        }
        lines[lines_count] = strdup(strtok(line, " "));
        lines_count++;
    }

    fclose(data_file);

    CacheSimulator* cache_sim;
    cache_sim = (CacheSimulator*)malloc(sizeof(CacheSimulator));
    if (cache_sim == NULL) {
        perror("Error allocating memory");
        return 1;
    }
    // printf("%d\n", lines_count);
    for (int cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        cache_sim->cache_slots = cache_slots;
        cache_sim->cache_hit = 0;
        cache_sim->tot_cnt = 1;
        initCircularLinkedList(&(cache_sim->container));
        for (int i = 0; i < lines_count; ++i) {
        // printf("%d\n", size(&(cache_sim->container)));
            do_sim(cache_sim, lines[i]);
        }

        print_stats(cache_sim);
    }

    free(cache_sim); // CacheSimulator 메모리 해제
    free(lines);

    return 0;
}
