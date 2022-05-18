#include <exception>
#include "BagIterator.h"
#include "Bag.h"

#define NULL_TELEM -111111

using namespace std;


BagIterator::BagIterator(const Bag& c): bag(c){
    this->current = 0;
    this->currentFreq = this->bag.table[this->current].second;
    this->count = 1;
    this->oldHead = 0;

}

void BagIterator::first() {
    this->current = 0;
    this->currentFreq = this->bag.table[this->current].second;
    this->count = 1;
    this->oldHead = 0;

}


void BagIterator::next() {
    if(!valid())
        throw exception();

    if(this->currentFreq > 1)
        this->currentFreq--;

    else {
        if (this->bag.next[this->current] != NULL_TELEM) {
            this->oldHead = this->current;
            this->current = this->bag.next[this->current];
            this->currentFreq = this->bag.table[this->current].second;
            this->count++;

        }

        else{
            this->current = this->oldHead;
            this->current++;
            this->oldHead = this->current;
            this->count++;

            while(this->bag.table[this->current].first == NULL_TELEM) {
                this->current++;
                this->oldHead = this->current;

            }

            this->currentFreq = this->bag.table[this->current].second;

        }

    }

}


bool BagIterator::valid() const {
    return this->current < this->bag.m && this->count+1 < this->bag.n;

}



TElem BagIterator::getCurrent() const{
    if(!valid())
        throw exception();

    return this->bag.table[this->current].first;

}
