#include <stdio.h>
#include <limits.h>
#include <malloc.h>
int *worst_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        int curr_proc = proc_map[i];
        int idx = -1, diff = INT_MIN;
        for (int j = 0; j < mem_size; ++j)
        {
            if (mem_map_copy[j] >= curr_proc && mem_map_copy[j] - curr_proc > diff && mem_map_copy[j] == mem_map[j])
            {
                idx = j;
                diff = mem_map_copy[j] - curr_proc;
            }
        }
        if (idx != -1)
        {
            mem_map_copy[idx] -= curr_proc;
            result[i] = mem_map_copy[idx];
        }
    }
    free(mem_map_copy);
    return result;
}
int *first_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        int curr_proc = proc_map[i];
        for (int j = 0; j < mem_size; ++j)
        {
            if (mem_map_copy[j] >= curr_proc && mem_map_copy[j] == mem_map[j])
            {
                mem_map_copy[j] -= curr_proc;
                result[i] = mem_map_copy[j];
                break;
            }
        }
    }
    free(mem_map_copy);
    return result;
}
int *best_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        int curr_proc = proc_map[i];
        int idx = -1, diff = INT_MAX;
        for (int j = 0; j < mem_size; ++j)
        {
            if (mem_map_copy[j] >= curr_proc && mem_map_copy[j] - curr_proc < diff && mem_map_copy[j] == mem_map[j])
            {
                idx = j;
                diff = mem_map_copy[j] - curr_proc;
            }
        }
        if (idx != -1)
        {
            mem_map_copy[idx] -= curr_proc;
            result[i] = mem_map_copy[idx];
        }
    }
    free(mem_map_copy);
    return result;
}
int *next_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    int next_idx = 0;
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        for (int j = next_idx, k = 0; k < mem_size; j = (j + 1) % mem_size, ++k)
        {
            if (mem_map_copy[j] >= proc_map[i] && mem_map_copy[j] == mem_map[j])
            {
                mem_map_copy[j] -= proc_map[i];
                result[i] = mem_map_copy[j];
                if (mem_map_copy[j] != 0)
                    next_idx = j;
                else
                    next_idx = (j + 1) % mem_size;
                break;
            }
        }
    }
    free(mem_map_copy);
    return result;
}
int main()
{
    int *mem_map, *proc_map;
    int mem_size, proc_size;
    printf("Enter size of memory map: \n");
    scanf("%d", &mem_size);
    printf("Enter size of process map: \n");
    scanf("%d", &proc_size);
    mem_map = (int *)malloc(sizeof(int) * mem_size);
    proc_map = (int *)malloc(sizeof(int) * proc_size);
    printf("Enter sizes of memory map: \n");
    for (int i = 0; i < mem_size; ++i)
        scanf("%d", &mem_map[i]);
    printf("Enter sizes of process map: \n");
    for (int i = 0; i < proc_size; ++i)
        scanf("%d", &proc_map[i]);
    int *best_fit = best_fit_map(mem_map, proc_map, mem_size, proc_size);
    int *first_fit = first_fit_map(mem_map, proc_map, mem_size, proc_size);
    int *worst_fit = worst_fit_map(mem_map, proc_map, mem_size, proc_size);
    int *next_fit = next_fit_map(mem_map, proc_map, mem_size, proc_size);
    // Logic to print above three arrays as table
    printf("PROC SIZE\t BEST FIT\t FIRST FIT\t WORST FIT\t NEXT FIT\n");
    for (int i = 0; i < proc_size; ++i)
        printf("%d\t\t %d\t\t %d\t\t %d\t\t %d\n", proc_map[i], best_fit[i], first_fit[i], worst_fit[i], next_fit[i]);
    free(best_fit);
    free(first_fit);
    free(worst_fit);
    free(mem_map);
    free(proc_map);
    return 0;
}
