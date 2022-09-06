#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <limits.h>
int myAtoi(char *s){
    size_t num = 0, sign = 0;
	while(isspace(*s))s++;
	switch (*s) {
	case '-': sign=1;
	case '+': s++;
	}
    while ((isdigit(*s) && num < INT_MAX)) 
		num = num * 10 + ((*s++) - '0');
	return  (sign == 1) ? ((num > INT_MAX) ? INT_MIN : -num) : ((num > INT_MAX) ? INT_MAX : num);
}
