#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <map>

SMMIterator::SMMIterator(const SortedMultiMap &d) : map(d) {
    this->current = d.head;
    this->index = 0;

}

void SMMIterator::first() {
    this->current = this->map.head;
    this->index = 0;

}

void SMMIterator::next() {
    if(!valid())
        throw std::exception();

    this->current = this->current->next;
    this->index++;

}

bool SMMIterator::valid() const {
    return this->index < this->map.listSize;

}

TElem SMMIterator::getCurrent() const {
    if(!valid())
        throw std::exception();

    return this->current->val;

}


