#include "Matrix.h"
#include <exception>
using namespace std;


Matrix::Matrix(int nrLines, int nrCols) {
    ///
    /// Complexity = Theta(1)
    ///

    this->noLines = nrLines;
    this->noCols = nrCols;
    this->size = 2;
    this->capacity = 2;

    this->lines = new int[this->noLines + 1]{NULL_TELEM};
    this->cols = new int[this->noCols]{NULL_TELEM};
    this->values = new TElem[this->noCols]{NULL_TELEM};

}

Matrix::~Matrix() {
    ///
    /// Complexity = Theta(1)
    ///

    delete this->lines;
    delete this->cols;
    delete this->values;

}


int Matrix::nrLines() const {
    ///
    /// Complexity = Theta(1)
    ///

    return this->noLines;

}


int Matrix::nrColumns() const {
    ///
    /// Complexity = Theta(1)
    ///

	return this->noCols;

}


TElem Matrix::element(int i, int j) const {
    ///
    /// Best Case (Element is the first one in the matrix) = Theta(1)
    /// Worst Case (Element doesn't exist or is the last one) = Theta(lines[i+1] - lines[i])
    /// Average Case = Theta(lines[i+1] - lines[i])
    /// Total: O(lines[i+1] - lines[i])
    ///

	if(i < 0 || i > this->noLines || j < 0 || j > this->noCols)
        throw exception();

    int start = this->lines[i];
    int end;

    if(i+1 >= this->noLines)
        end = capacity;

    else
        end = this->lines[i+1];

    while(start < end){
        if(this->cols[start] == j)
            return this->values[start];

        start++;

    }

    return NULL_TELEM;

}

void Matrix::resize() {
    ///
    /// Complexity = Theta(size)
    ///

    auto newCols = new TElem[(int)(this->size * 1.5)];
    auto newValues = new TElem[(int)(this->size * 1.5)];

    this->capacity = this->capacity * 1.5;

    for(int i = 0; i < this->size; ++i) {
        newCols[i] = this->cols[i];
        newValues[i] = this->values[i];

    }

    for(int i = this->size; i < this->capacity; i++){
        newCols[i] = NULL_TELEM;
        newValues[i] = NULL_TELEM;

    }

    delete[] this->values;
    delete[] this->cols;

    this->values = newValues;
    this->cols = newCols;

}

TElem Matrix::modify(int i, int j, TElem e) {
    ///
    /// Best Case (TElem e exists and is the first one in the matrix) = Theta(1)
    /// Worst Case (TElem e doesn't exist) = Theta(lines[i+1] - lines[i])
    /// Average Case = Theta(lines[i+1] - lines[i])
    /// Total: O(lines[i+1] - lines[i])
    ///

    if(i < 0 || i > this->noLines || j < 0 || j > this->noCols)
        throw exception();

    int start = this->lines[i];
    int end;

    if(i+1 >= this->noLines)
        end = size;

    else
        end = this->lines[i+1];

    int copy = NULL_TELEM;

    while(start < end) {
        if(this->cols[start] == j) {
            copy = this->values[start];
            if(e != NULL_TELEM)
                this->values[start] = e;
            else
                this->removeElem(i, start);

            return copy;

        }

        if(this->cols[start] > j) {

            copy = this->values[start];

            this->addElem(start, i, j, e);

            return copy;

        }

        start++;

    }

    this->addElem(start, i, j, e);

    return NULL_TELEM;

}

void Matrix::addElem(int start, int i, int j, TElem e) {
    ///
    /// Complexity = Theta(size)
    ///

    if(++this->size > this->capacity)
        this->resize();

    for(int index = this->size - 1; index > start; index--) {
        this->cols[index] = this->cols[index - 1];
        this->values[index] = this->values[index-1];

    }

    for(int index = i + 1; index < this->noLines; index++)
        this->lines[index]++;

    this->cols[start] = j;
    this->values[start] = e;

}


void Matrix::removeElem(int i, int j) {
    ///
    /// Complexity = Theta(size)
    ///

    for(int _j = j; _j < this->size; ++_j) {
        this->cols[_j] = this->cols[_j + 1];
        this->values[_j] = this->values[_j + 1];

    }

    for(int index = i + 1; index <= this->noLines; ++index)
        this->lines[index]--;

}