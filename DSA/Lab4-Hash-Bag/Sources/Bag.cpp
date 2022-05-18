#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;


Bag::Bag() {
	this->m = 10;
    this->n = 0;

    this->table = new std::pair<TElem, int>[this->m];
    this->next = new int[this->m];

    for(int i = 0; i < m; i++){
        this->table[i] = {NULL_TELEM,0};
        this->next[i] = -1;

    }

}

void Bag::add(TElem elem) {
    int pos = hash(elem, this->m);
    if(this->table[pos].first == NULL_TELEM){
        this->table[pos].first = elem;
        this->table[pos].second = 1;
        this->next[pos] = NULL_TELEM;

    }

    else{
        if(this->n > this->m/3)
            resize();

        pos = hash(elem, this->m);
        firstEmpty = getFirstEmpty();
        int current = pos;

        while(this->next[current] != NULL_TELEM && this->table[pos].first != elem)
            current = this->next[current];

        if(this->table[pos].first == elem)
            this->table[pos].second++;

        else {
            this->table[this->firstEmpty].first = elem;
            this->table[this->firstEmpty].second++;
            this->next[this->firstEmpty] = NULL_TELEM;
            this->next[current] = this->firstEmpty;

        }

    }

    this->n++;

}

bool Bag::remove(TElem elem) {
    int pos = hash(elem, this->m);
    int prev = -1;

    if(this->table[pos].first == NULL_TELEM)
        return false;

    while(this->next[pos] != NULL_TELEM && this->table[pos].first != elem) {
        prev = pos;
        pos = this->next[pos];

    }

    // we found the key
    if(this->table[pos].second != 1)
        this->table[pos].second--;

    else {
        this->table[pos] = {NULL_TELEM, 0};

        if (this->next[prev] == pos)
            this->next[prev] = this->next[pos];

        else {
            while (this->next[pos] != NULL_TELEM) {
                this->table[pos] = this->table[this->next[pos]];
                pos = this->next[pos];


            }

            this->table[pos] = {NULL_TELEM, 0};

        }

        this->next[pos] = NULL_TELEM;

    }

    this->n--;

    return true;

}

bool Bag::search(TElem elem) const {
    int pos = hash(elem, this->m);

    if(this->table[pos].first == NULL_TELEM)
        return false;

    while(pos != NULL_TELEM && this->table[pos].first != elem)
        pos = this->next[pos];

    if(pos == NULL_TELEM)
        return false;

    return true;

}

int Bag::nrOccurrences(TElem elem) const {
    int pos = hash(elem, this->m);

    if(this->table[pos].first == NULL_TELEM)
        return 0;

    while(pos != NULL_TELEM && this->table[pos].first != elem)
        pos = this->next[pos];

    if(pos == NULL_TELEM)
        return 0;

    return this->table[pos].second;

}

int Bag::size() const {
	return this->n;

}

bool Bag::isEmpty() const {
	return this->n == 0;

}

BagIterator Bag::iterator() const {
	return BagIterator(*this);
}


Bag::~Bag() {
	delete[] this->table;
    delete[] this->next;

}

int Bag::hash(int k, int cap) const {
    return ((k %= cap) < 0) ? k+cap : k;

}

int Bag::getFirstEmpty() {
    for(int i = this->m - 1; i >= 0; i--)
        if(this->table[i].first == NULL_TELEM)
            return i;

    return -1;

}

void Bag::resize(){
    std::pair<TElem,int>* newTable = new std::pair<TElem,int>[this->m * 2];
    int* newNext = new int[this->m * 2];
    int newFirstEmpty = this->m * 2 - 1;

    for(int i = 0; i < m*2; i++){
        newTable[i] = {NULL_TELEM,0};
        newNext[i] = NULL_TELEM;

    }

    for(int i = 0; i < m; i++){
        if(this->table[i].first != NULL_TELEM) {
            int pos = hash(this->table[i].first, m * 2);
            newTable[pos] = this->table[i];
            //newNext[pos] = this->next[pos];

        }

    }

    this->m *= 2;

    delete[] this->table;
    delete[] this->next;

    this->table = newTable;
    this->next = newNext;

}
