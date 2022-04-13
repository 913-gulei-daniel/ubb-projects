#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <map>

SMMIterator::SMMIterator(const SortedMultiMap &d) : map(d) {
    ///
    /// Complexity = Theta(1)
    ///

    this->current = d.head;
    this->index = 0;

}

void SMMIterator::first() {
    ///
    /// Complexity = Theta(1)
    ///

    this->current = this->map.head;
    this->index = 0;

}

void SMMIterator::next() {
    ///
    /// Complexity = Theta(1)
    ///

    if(!valid())
        throw std::exception();

    this->current = this->current->next;
    this->index++;

}

bool SMMIterator::valid() const {
    ///
    /// Complexity = Theta(1)
    ///

    return this->index < this->map.listSize;

}

TElem SMMIterator::getCurrent() const {
    ///
    /// Complexity = Theta(1)
    ///

    if(!valid())
        throw std::exception();

    return this->current->val;

}


