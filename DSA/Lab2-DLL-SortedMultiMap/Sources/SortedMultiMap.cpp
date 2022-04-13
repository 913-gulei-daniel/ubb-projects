#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>

using namespace std;

SortedMultiMap::SortedMultiMap(Relation r) {
    this->head = nullptr;
    this->tail = nullptr;
    this->rel = r;
    this->listSize = 0;

}

void SortedMultiMap::add(TKey c, TValue v) {
    ///
    /// Complexity = Theta(1)
    ///

    node* newNode = new node;
    node* current = this->head;

    newNode->val = std::make_pair(c, v);
    newNode->next = nullptr;
    newNode->prev = nullptr;

    if(this->head == nullptr){
        this->head = newNode;
        this->tail = newNode;

    }

    else if(this->rel(c, this->head->val.first)){
        newNode->prev = nullptr;
        newNode->next = this->head;
        this->head->prev = newNode;
        this->head = newNode;

    }

    else{
        while(current != nullptr && !this->rel(c, current->val.first))
            current = current->next;

        if(current == nullptr){
            // insert as new tail
            newNode->prev = this->tail;
            newNode->next = nullptr;
            this->tail->next = newNode;
            this->tail = newNode;

        }

        else{
            newNode->prev = current->prev;
            newNode->next = current;
            current->prev->next = newNode;
            current->prev = newNode;

        }

    }

    this->listSize++;

}

vector <TValue> SortedMultiMap::search(TKey c) const {
    ///
    /// Complexity = Theta(n) (where n is the size of the DLL)
    ///

    node* current = this->head;
    vector<TValue> arr;

    arr.clear();

    while(current != nullptr) {
        if(current->val.first == c)
            arr.push_back(current->val.second);

        current = current->next;


    }

    return arr;

}

bool SortedMultiMap::remove(TKey c, TValue v) {
    ///
    /// Complexity = O(n)
    ///

    TElem elem = std::make_pair(c, v);

    node* current = this->head;
    bool deleted;

    while(current != nullptr && current->val != elem)
        current = current->next;

    if(current != nullptr) {
        if (current == this->head) {
            if (current == this->tail) {
                this->head = nullptr;
                this->tail = nullptr;

            } else {
                this->head = this->head->next;
                this->head->prev = nullptr;

            }

        }

        else if (current == this->tail) {
            this->tail = this->tail->prev;
            this->tail->next = nullptr;

        }

        else {
            current->next->prev = current->prev;
            current->prev->next = current->next;

        }

        delete current;
        this->listSize--;
        deleted = true;

    }

    else
        deleted = false;

    return deleted;
}


int SortedMultiMap::size() const {
    ///
    /// Complexity = Theta(1)
    ///

    return this->listSize;

}

bool SortedMultiMap::isEmpty() const {
    ///
    /// Complexity = Theta(1)
    ///

    return this->head == nullptr;
}

SMMIterator SortedMultiMap::iterator() const {
    return SMMIterator(*this);

}

SortedMultiMap::~SortedMultiMap() {
    ///
    /// Complexity = Theta(n) (where n is the size of the list)
    ///

    while(this->head != nullptr){
        node* aux = this->head;
        this->head = this->head->next;
        delete aux;

    }

}
