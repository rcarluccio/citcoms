// -*- C++ -*-
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//  <LicenseText>
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#if !defined(pyCitcom_Exchanger_h)
#define pyCitcom_Exchanger_h

#include "mpi.h"


class Boundary;
struct All_variables;

struct Data {
    static const int npass = 4;  // # of arrays to send/receive
    int size;                    // length of each array
    double *v[3];                // velocities
    double *T;                   // temperature
    //double *P;                   // pressure
};


class Exchanger {

public:
    Exchanger(const MPI_Comm comm,
	      const MPI_Comm intercomm,
	      const int leader,
	      const int localLeader,
	      const int remoteLeader,
	      const All_variables *E);
    virtual ~Exchanger();

    void createDataArrays();
    void deleteDataArrays();

    void initTemperature();
    void sendTemperature();
    void receiveTemperature();
    void sendVelocities();
    void receiveVelocities();

    void imposeBC();
    void setBCFlag();

    void storeTimestep(const double fge_time, const double cge_time);
    double exchangeTimestep(const double) const;
    int exchangeSignal(const int) const;

    virtual void gather() = 0;
    virtual void distribute() = 0;
    virtual void interpretate() = 0;  // interpolate or extrapolate
    //virtual void imposeBC() = 0;      // set bc flag
    virtual void mapBoundary() = 0;   // create mapping from Boundary object
                                      // to global id array

protected:
    const MPI_Comm comm;       // communicator of current solver
    const MPI_Comm intercomm;  // intercommunicator between solvers

    const int rank;            // proc. rank in comm
    const int leader;          // leader rank (in comm) of current solver

    const int localLeader;     // leader rank (in intercomm) of current solver
    const int remoteLeader;    // leader rank (in intercomm) of another solver

    const All_variables *E;    // CitcomS data structure,
                               // Exchanger only modifies bc flags directly
	                       // and id array indirectly
    Boundary *boundary;

    struct Data outgoing;
    struct Data incoming;
    struct Data loutgoing;
    struct Data lincoming;
    struct Data poutgoing;

    double fge_t, cge_t;

    void printDataT(const Data &data) const;
    void printDataV(const Data &data) const;
    void imposeConstraint();

private:
    double exchangeDouble(const double &sent, const int len) const;
    float exchangeFloat(const float &sent, const int len) const;
    int exchangeInt(const int &sent, const int len) const;

    // disable copy constructor and copy operator
    Exchanger(const Exchanger&);
    Exchanger operator=(const Exchanger&);


};



#endif

// version
// $Id: ExchangerClass.h,v 1.26 2003/10/05 18:55:48 tan2 Exp $

// End of file

